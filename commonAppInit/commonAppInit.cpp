/**
 * An attempt to abstract some of the platform specific code that happens on
 * startup and shutdown.
 **/

#include "commonAppInit/commonAppInit.hpp"

#include <log4cplus/logger.h>
#include <log4cplus/loggingmacros.h>
#include <log4cplus/configurator.h>

#include <boost/program_options.hpp>

namespace projectnamespace { namespace commonAppInit {

int CommonAppInit::Main(const boost::program_options::variables_map& commandLineArgs)
{
    /**
    if (vm.count("help"))
    {
        std::cout << commandLineArgs << std::endl;
        return 0;
    }
    **/
    InitialiseLoggingSystem(commandLineArgs);

    /**
    if (!Init(commandLineArgs) ||
        !LoadSettings(commandLineArgs) ||
        !StartUpAppLayer(commandLineArgs))
    {
        Shutdown(commandLineParams);
        return 1;
    }

    // TODO: app layers main method.

    Shutdown(commandLineParams);

    // logging system apparently doesnt need any shutdown.... 
    **/

    return 0;
}

void CommonAppInit::PopulateCommandLineOptions(
    boost::program_options::options_description& options)
{
    options.add_options()
        ("help", "print this help message and exit."); 
}

// logging is a non-platform specific system that all applications will expect
// to be setup..
void CommonAppInit::InitialiseLoggingSystem(
    const boost::program_options::variables_map& commandLineArgs)
{
    log4cplus::BasicConfigurator configurator;
    configurator.configure();

    log4cplus::Logger logger = log4cplus::Logger::getInstance(LOG4CPLUS_TEXT("CommonAppInit"));
    LOG4CPLUS_INFO(logger, LOG4CPLUS_TEXT("Logging system initialised...")); 
}

bool StartUpAppLayer(const boost::program_options::variables_map& commandLineParams)
{
    // TODO: create the app layer and run its Setup method.
    return true;
}

}}
