#pragma once

#ifdef BL_PLATFORM_WINDOWS
    #ifdef BL_BUILD_DLL
        #define BLINKY_API __declspec(dllexport)
    #else
        #define BLINKY_API __declspec(dllimport)
    #endif
#else
    #error Only windows is supported
#endif

#define BIT(x) (1 << x)