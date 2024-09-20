{ pkgs, ... }:

{
  packages = [
    pkgs.hatch
  ];

  languages.python = {
    enable = true;
    version = "3.12";
    venv.enable = false;
  };

  enterShell = ''
    hatch run true  # Create virtualenv at first run
    export VIRTUAL_ENV="$(hatch env find)"
    export HATCH_ENV_ACTIVE=default
    export PATH="$VIRTUAL_ENV/bin:$PATH"
  '';
}
