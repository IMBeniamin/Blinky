project "Sandbox"
	kind "ConsoleApp"
	language "C++"
	cppdialect "C++17"
	staticruntime "off"

	targetdir ("%{wks.location}/bin/" .. outputdir .. "/%{prj.name}")
	objdir ("%{wks.location}/bin-int/" .. outputdir .. "/%{prj.name}")

	files
	{
		"src/**.h",
		"src/**.cpp"
	}

	includedirs
	{
		"%{IncludeDir.Spdlog}",
		"%{wks.location}/Blinky/src",
		"%{wks.location}/Blinky/vendor",
		"%{IncludeDir.glm}"
	}

	links
	{
		"Blinky"
	}

	filter "system:windows"
		systemversion "latest"

	filter "configurations:Debug"
		defines "BL_DEBUG"
		runtime "Debug"
		symbols "on"
		
		postbuildcommands
		{
			
		}

	filter "configurations:Release"
		defines "BL_RELEASE"
		runtime "Release"
		optimize "on"

	filter "configurations:Dist"
		defines "BL_DIST"
		runtime "Release"
		optimize "on"