{ pkgs }: {
  deps = [
    pkgs.puppet-lint
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
  ];
}