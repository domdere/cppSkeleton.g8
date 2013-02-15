#!/usr/bin/python

from optparse import OptionParser, OptionGroup

def versionString():
    return '1.0'

def usageString():
    return '%prog [options] output\n\
    Where:\n\
        \'output\' is the destination codegen file to write this info to\n\
\n\
    Generates a cxx file that will embed versioning data in a C++ app'

def setopts():
    parser = OptionParser(usage=usageString(), version=versionString())

    repoVersioningOptions = OptionGroup(
        parser,
        "Repo and Source control options",
        "Allows you to specify information required for embedding version info about your app")

    repoVersioningOptions.add_option('--git', type='string', dest='gitinfo', default='', nargs=2,
        help='Info for getting the git versioning info, where GITEXE is the path to the git binary \
and REPO_PATH is the path to the repo from which the build is being made, if nothing is provided it will skip the git versioning',
        metavar='\"GITEXE REPO_PATH\"')

    parser.add_option_group(repoVersioningOptions)

    externalLibs = OptionGroup(
        parser,
        "External Libs",
        "Allows you to specify version numbers for external libraries that were built separately")

    externalLibs.add_option("--boost", type='string', dest='boostversion', default='',
        help='Boost version.  Library providing a wide set of functionality to C++, http://www.boost.org/',
        metavar='VERSION')
    
    externalLibs.add_option("--hdf5", type='string', dest='hdf5version', default='',
        help='HDF5 version.  Library that helps read and write to and from hdf5 files, a format that provides fast lookup to large collections of data, http://www.hdfgroup.org/HDF5/',
        metavar='VERSION')

    externalLibs.add_option("--json_spirit", type='string', dest='jsonspiritversion', default='',
        help='Json Spirit version.  Library built on top of the Boost Spirit library providing the ability to build and parse JSON objects to and from strings',
        metavar='VERSION')
    
    externalLibs.add_option("--log4cplus", type='string', dest='log4cplusversion', default='',
        help='Log4Cplus.  Logging library, http://log4cplus.sourceforge.net/',
        metavar='VERSION')
    
    externalLibs.add_option("--soci", type='string', dest='sociversion', default='',
            help='Soci version.  Library providing database access functionality, http://soci.sourceforge.net',
        metavar='VERSION')
    
    externalLibs.add_option("--poco", type='string', dest='pocoversion', default='',
        help='Poco version.  Library providing a wide set of networking functionality (e.g socket wrappers and http servers and clients) to C++, http://pocoproject.org',
        metavar='VERSION')
    
    parser.add_option_group(externalLibs)

    miscOpts = OptionGroup(parser, "Miscellaneous Options")

    miscOpts.add_option

    parser.add_option_group(miscOpts)

    return parser

def main():

    parser = setopts()

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error('Invalid number of args, expected 1 args, received ' + str(len(args)))

    outputFilename = args[0]

    versionInfo

    return

if __name__ == '__main__':
    main()
