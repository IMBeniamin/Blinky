#pragma once

#include "Core.h"
#include "Blinky/Base.h"

#include "spdlog/spdlog.h"
#include "spdlog/fmt/ostr.h"

namespace Blinky {
	class BLINKY_API Log
	{
	private:
		static std::shared_ptr<spdlog::logger> s_CoreLogger;
		static std::shared_ptr<spdlog::logger> s_ClientLogger;

	public:
		static void Init();
		inline static std::shared_ptr<spdlog::logger>& GetCoreLogger() { return s_CoreLogger; }
		inline static std::shared_ptr<spdlog::logger>& GetClientLogger() { return s_ClientLogger; }

	};
};
// Core log macros

#define BL_CORE_TRACE(...) ::Blinky::Log::GetCoreLogger()->trace(__VA_ARGS__)
#define BL_CORE_INFO(...)  ::Blinky::Log::GetCoreLogger()->info(__VA_ARGS__)
#define BL_CORE_WARN(...)  ::Blinky::Log::GetCoreLogger()->warn(__VA_ARGS__)
#define BL_CORE_ERROR(...) ::Blinky::Log::GetCoreLogger()->error(__VA_ARGS__)
#define BL_CORE_FATAL(...) ::Blinky::Log::GetCoreLogger()->critical(__VA_ARGS__)

// Client log macros

#define BL_TRACE(...)      ::Blinky::Log::GetClientLogger()->trace(__VA_ARGS__)
#define BL_INFO(...)       ::Blinky::Log::GetClientLogger()->info(__VA_ARGS__)
#define BL_WARN(...)       ::Blinky::Log::GetClientLogger()->warn(__VA_ARGS__)
#define BL_ERROR(...)      ::Blinky::Log::GetClientLogger()->error(__VA_ARGS__)
#define BL_FATAL(...)      ::Blinky::Log::GetClientLogger()->critical(__VA_ARGS__)
