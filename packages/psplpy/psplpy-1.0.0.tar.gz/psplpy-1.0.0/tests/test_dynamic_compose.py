if __name__ == '__main__':
    from __init__ import *
else:
    from . import *
from psplpyProject.psplpy.dynamic_compose import DynamicCompose

dc_rc_dir = rc_dir / 'dynamic_compose'
compose_dumped_file = dc_rc_dir / 'compose-dumped.yml'
dockerfile_dumped_file = dc_rc_dir / 'Dockerfile-dumped'


def tests():
    DynamicCompose.CWD = dc_rc_dir
    dc = DynamicCompose()

    dc.compose_file = tmp_dir / 'compose.yml'
    dc.dockerfile_file = tmp_dir / 'Dockerfile'

    dc.format_compose(template_file=dc.CWD / 'compose-template.yml')
    dc.format_dockerfile(template_file=dc.CWD / 'Dockerfile-template')

    dc.dump()

    assert compose_dumped_file.read_text().strip() == dc.compose_file.read_text().strip()
    dc.compose_file.unlink()
    assert dockerfile_dumped_file.read_text().strip() == dc.dockerfile_file.read_text().strip()
    dc.dockerfile_file.unlink()


if __name__ == '__main__':
    tests()
