#pragma once

#ifdef BL_PLATFORM_WINDOWS

extern Blinky::Application* Blinky::CreateApplication();

int main(int argc, char ** argv)
{
	Blinky::Log::Init();
	BL_CORE_WARN("Initialized Log");
	BL_WARN("Initialized Log");
	auto app = Blinky::CreateApplication();
	app->Run();
	delete app;
}

#endif