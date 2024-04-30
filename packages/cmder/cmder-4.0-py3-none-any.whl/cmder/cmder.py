#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A shortcut for running shell command.
"""
import argparse
import subprocess
import os
import sys
import shlex
import tempfile
from pathlib import Path

CMD_LINE_LENGTH = 100
PMT = False

try:
    from loguru import logger
    logger.remove()
    logger.add(sys.stderr, format="<level>{message}</level>", filter=lambda record: record["level"].name == "DEBUG")
    logger.add(sys.stderr, format="<light-green>[{time:HH:mm:ss}]</light-green> <level>{message}</level>", level="INFO")
except ImportError:
    import logging
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logger = logging.getLogger()


def run(cmd, **kwargs):
    """ Run cmd or raise exception if run fails. """
    def format_cmd(command):
        if isinstance(command, str):
            command = shlex.shlex(command, posix=True, punctuation_chars=True)
            command.whitespace_split = True
            command = list(command)
        elif isinstance(command, (list, tuple)):
            command = [str(c) for c in command]
        else:
            raise TypeError('Command only accepts a string or a list (or tuple) of strings.')
        exe = command[0]
        if len(' '.join(command)) <= CMD_LINE_LENGTH:
            return exe, ' '.join(command)
        command = ' '.join([f'\\\n  {c}' if c.startswith('-') or '<' in c or '>' in c else c for c in command])
        command = command.splitlines()
        commands = []
        for i, c in enumerate(command):
            if i == 0:
                commands.append(c)
            else:
                if len(c) <= 80:
                    commands.append(c)
                else:
                    items = c.strip().replace(' \\', '').split()
                    commands.append(f'  {items[0]} {items[1]} \\')
                    for item in items[2:]:
                        commands.append(' ' * (len(items[0]) + 3) + item + ' \\')
        command = '\n'.join(commands)
        if command.endswith(' \\'):
            command = command[:-2]
        return exe, command
    
    def parse_profile():
        try:
            with open(profile_output) as f:
                t, m = f.read().strip().split()
                t = t.split(".")[0]
                try:
                    hh, mm, ss = t.split(':')
                except ValueError:
                    hh, (mm, ss) = 0, t.split(':')
                t = f'{int(hh):02d}:{int(mm):02d}:{int(ss):02d}'
                m = float(m)
                if m < 1000:
                    m = f'{m:.2f}KB'
                elif m < 1000 * 1000:
                    m = f'{m / 1000:.2f}MB'
                else:
                    m = f'{m / 1000 / 1000:.2f}GB'
                s = f'{t} {m}'
        except FileNotFoundError:
            s = '00:00:00 0.00KB'
        return s
    
    msg, pmt, fmt_cmd = kwargs.pop('msg', ''), kwargs.pop('pmt', False), kwargs.pop('fmt_cmd', True)
    log_cmd, debug = kwargs.pop('log_cmd', True), kwargs.pop('debug', False)
    exit_on_error = kwargs.pop('exit_on_error', False)
    if fmt_cmd:
        program, cmd = format_cmd(cmd)
    else:
        if isinstance(cmd, str):
            program, cmd = cmd.split()[0], cmd
        else:
            program, cmd = cmd[0], ' '.join([str(c) for c in cmd])
    if msg:
        logger.info(msg)
    if log_cmd:
        logger.debug(cmd)
    cwd = kwargs.pop('cwd', None)
    profile_output = tempfile.mktemp(suffix='.txt', prefix='.profile.', dir=cwd)
    try:
        if msg and (pmt or PMT):
            cmd = f'/usr/bin/time -f "%E %M" -o {profile_output} {cmd}'
        kwargs['stdout'] = kwargs.pop('stdout', sys.stdout if debug else subprocess.PIPE)
        kwargs['stderr'] = kwargs.pop('stderr', sys.stderr if debug else subprocess.PIPE)
        process = subprocess.Popen(cmd, universal_newlines=True, shell=True, cwd=cwd, **kwargs)
        process.wait()
        if process.returncode: 
            stdout, stderr = process.communicate()
            logger.error(f'Failed to run {program} (exit code {process.returncode}):\n{stderr or stdout}')
            if exit_on_error:
                sys.exit(process.returncode)
        if not process.returncode and msg:
            msg = msg.replace(' ...', f' complete.')
            if pmt or PMT:
                msg = f'{msg[:-1]} [{parse_profile()}].' if msg.endswith('.') else f'{msg} [{parse_profile()}].'
            logger.info(msg)
    finally:
        if os.path.isfile(profile_output):
            os.unlink(profile_output)
    return process


def cmd(**kwargs):
    exe, sep = kwargs.pop('exe', ''), kwargs.pop('sep', ' ')
    includes, excludes, = kwargs.pop('includes', []), kwargs.pop('excludes', [])
    if includes:
        kwargs = {k: v for k, v in kwargs.items() if k in includes}
    cmds = [exe]
    for k, v in kwargs.items():
        if k in excludes:
            continue
        if isinstance(v, bool):
            if v:
                cmds.append(f'--{k}')
        elif isinstance(v, (list, tuple, set)):
            cmds.append(f'--{k} {" ".join(str(x) for x in v)}')
        else:
            if v:
                cmds.append(f'--{k} {v}')
    return sep.join(cmds)


def submit(command, **kwargs):
    try:
        script = Path(kwargs.get('script', 'submit.sh')).resolve()
        logger.info(f'Generating submission script {script}')
        nodes = kwargs.get('nodes', 1)
        ntasks_per_node = kwargs.get('ntasks_per_node', 1)
        ntasks = kwargs.get('ntasks', 1)
        queue = kwargs.get('queue', '')
        day = kwargs.get('day', 1)
        hour = kwargs.get('hour', 1)

        with script.open('w') as o:
            o.write('#!/usr/bin/env bash\n')
            o.write('\n')
            o.write(f'#SBATCH --nodes={nodes}\n')
            o.write(f'#SBATCH --ntasks={ntasks}\n')
            o.write(f'#SBATCH --ntasks-per-node={ntasks_per_node}\n')
            o.write(f'#SBATCH --time={day}-{hour}:59\n')
            o.write(f'#SBATCH --partition={queue}\n')
            
            cpus_per_node = kwargs.get('cpus_per_node', '')
            if cpus_per_node:
                o.write(f'#SBATCH --cpus-per-node={cpus_per_node}\n')
            
            gpus_per_node = kwargs.get('gpus_per_node', '')
            if gpus_per_node:
                o.write(f'#SBATCH --gpus-per-node={gpus_per_node}\n')
            
            array = kwargs.get('array', '')
            if array:
                o.write(f'#SBATCH --array={array}\n')
            
            name = kwargs.get('name', '')
            if name:
                o.write(f'#SBATCH --job-name={name}\n')
            
            dependency = kwargs.get('dependency', 0)
            if dependency:
                o.write(f'#SBATCH --dependency={dependency}\n')
                o.write(f'#SBATCH --kill-on-invalid-dep=yes\n')
            
            email, mail = kwargs.get('email', ''), kwargs.get('mail', '')
            email_type, mail_type = kwargs.get('email_type', ''), kwargs.get('mail_type', '')
            if email or mail:
                o.write(f'#SBATCH --mail-user={email or mail}\n')
                o.write(f'#SBATCH --mail-type={email_type or mail_type}\n')
            
            log, log_mode = kwargs.get('log', '%x.log'), kwargs.get('log_mode', '')
            o.write(f'#SBATCH --output={log}\n')
            if log_mode:
                o.write(f'#SBATCH --open-mode={log_mode}\n')
            
            project, comment = kwargs.get('project', ''), kwargs.get('comment', '')
            if project and queue != 'gpu-a40':
                o.write(f'#SBATCH --account={project}\n')
            if comment:
                o.write(f'#SBATCH --comment={comment}\n')
            
            directives = kwargs.get('directives', [])
            if directives:
                for directive in directives:
                    o.write(f'{directive}\n')
            
            environments = kwargs.get('environments', [])
            if environments:
                for environment in environments:
                    o.write(f'{environment}\n')
            
            o.write(f'{cmd}\n\n')
        
        logger.info(f'Successfully generated submit script {script}')
        
        if kwargs.get('hold', False):
            logger.info(f'Script {script.name} has not been submitted due to hold is True\n')
            return 0, 0
        else:
            envs, env = kwargs.get('envs', {}), os.environ.copy()
            if envs:
                for k, v in envs.items():
                    env[k] = v
            p = run(f'sbatch {script.name}', cwd=script.parent, env=env)
            if p.returncode:
                logger.info(f'Failed to submit {script.name} to job queue due to an error\n')
                return p.returncode, 0
            else:
                s = p.stdout.read()
                try:
                    sid = int(s.strip().splitlines()[-1].split()[-1])
                    logger.info(f'Successfully submitted job with slurm job id {sid}\n')
                    return 0, sid
                except Exception as e:
                    logger.error(f'Failed to get job id from submit result due to {e}:\n\n{s}')
                    return 0, 0
    except Exception as e:
        logger.error(f'Failed to generate submit script and submit the job due to\n{e}\n\n')
        return 1, 0


if __name__ == '__main__':
    pass
