include "./vendor/premake/premake_customization/solution_items.lua"
include "Dependencies.lua"

workspace "Blinky"
	architecture "x86_64"
	startproject "Sandbox"

	configurations
	{
		"Debug",
		"Release",
		"Dist"
	}

	solution_items
	{
		".editorconfig"
	}

	flags
	{
		"MultiProcessorCompile"
	}

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

group "Dependencies"
	include "vendor/premake"
	include "Blinky/vendor/GLFW"
	include "Blinky/vendor/Glad"
	include "Blinky/vendor/imgui"
	include "Blinky/vendor/spdlog"
group ""

include "Blinky"
include "Sandbox"
