# Template

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Template.

## Description
Trying to figure out a workflow on clusters.

## Visuals
[MVP](assets/image.png)

## Installation
- [] TODO How to set up

## Usage
- [] TODO How to use

## Dependencies (see `install.sh`)
- Hydra
- mlflow
- https://github.com/facebookincubator/submitit
- https://hydra.cc/docs/plugins/submitit_launcher/

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## License
For open source projects, say how it is licensed.


## Pitfalls
- Default mounting of `$HOME` in apptainer:
    - During conda installation and initialization. Host `.bashrc` was modified. --> Opting for `apptained build --no-home ...`
- Apptainer support:
    - https://github.com/facebookincubator/submitit/issues/1608
    - https://github.com/facebookincubator/submitit/pull/1729
    - https://github.com/facebookincubator/submitit/pull/1729/files
        - My fix: add python: Optional[str]=None to `hydra_submitit/config.py`
- Overriding hydra/launcher:
    - https://github.com/facebookresearch/hydra/issues/1366
    - https://github.com/facebookresearch/hydra/issues/1565

## TODO
- [ ]
