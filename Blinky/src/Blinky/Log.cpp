#include "blpch.h"
#include "spdlog/sinks/stdout_color_sinks.h"
namespace Blinky {
	Ref<spdlog::logger> Log::s_CoreLogger;
	Ref<spdlog::logger> Log::s_ClientLogger;
	std::shared_ptr<spdlog::logger> Log::s_CoreLogger;
	std::shared_ptr<spdlog::logger> Log::s_ClientLogger;
	void Log::Init()
	{
		spdlog::set_pattern("%^[%t] %n: %v%$");
		s_CoreLogger = spdlog::stdout_color_mt("BLINKY");
		s_CoreLogger->set_level(spdlog::level::trace);
		s_ClientLogger = spdlog::stdout_color_mt("APP");
		s_ClientLogger->set_level(spdlog::level::trace);
	}
}
