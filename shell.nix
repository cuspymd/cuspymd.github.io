{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/a7ecde854aee5c4c7cd6177f54a99d2c1ff28a31.tar.gz") {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.ruby_3_0
  ];
}
