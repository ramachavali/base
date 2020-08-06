#!/bin/bash

set -o errexit
set -o nounset

usage() {
    [[ $# -gt 0 ]] && echo "$1" >&2 && echo >&2
    cat >&2 <<EOF
Descriptioin: this is what the scirpt does


Usage: $0 [options] requried_arg
supported options:
    -h       display this help
#example of option description
#   -t       test mode, run without deleting and show files that will be deleted.

Examples:
#example of how the scirpt is used with args and options

EOF
    [[ $# -gt 0 ]] && exit 1 || exit 0
}

. bash_funcs

# define defaults up front


# process arguments
while getopts ":h" opt; do
    case $opt in
        h)  usage;;
#        t)  test_mode=1;;
        \?) usage "Invalid option: -$OPTARG";;
        :)  usage "Option -$OPTARG requires an argument";;
    esac
done
shift $(($OPTIND - 1))

# check for requried positional args 
[[ $# -eq 2 ]] || usage "Expected 2 positional args"

log INFO "this is how you log INFOmation"
