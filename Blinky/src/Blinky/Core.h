#pragma once
#ifdef BL_PLATFORM_WINDOWS
    #if BL_DYNAMIC_LINK
        #ifdef BL_BUILD_DLL
            #define BLINKY_API __declspec(dllexport)
        #else
            #define BLINKY_API __declspec(dllimport)
        #endif
    #else
        #define BLINKY_API
    #endif
#else
    #error Only windows is supported
#endif


#ifdef BL_DEBUG
    #define BL_ENABLE_ASSERTS
#endif

#ifdef HZ_ENABLE_ASSERTS
    #define BL_ASSERT(x, ...) { if(!(x)) { BL_ERROR("Assertion Failed: {0}", __VA_ARGS__); __debugbreak(); } }
    #define BL_CORE_ASSERT(x, ...) { if(!(x)) { BL_CORE_ERROR("Assertion Failed: {0}", __VA_ARGS__); __debugbreak(); } }
#else
    #define BL_ASSERT(x, ...)
    #define BL_CORE_ASSERT(x, ...)
#endif


#define BIT(x) (1 << x)

#define BL_BIND_EVENT_FN(x) std::bind(&x, this, std::placeholders::_1)
