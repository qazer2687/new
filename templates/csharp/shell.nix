{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  # Packages
  packages = [
    pkgs.dotnet-sdk_7
  ];

  # Environment
  LD_LIBRARY_PATH = "$LD_LIBRARY_PATH:${pkgs.dotnet-sdk_7}/lib";
  PATH = "$PATH:~/.dotnet/tools";
  DOTNET_ROOT = "${pkgs.dotnet-sdk_7}";
}