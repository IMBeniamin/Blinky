#pragma once

#ifdef BL_PLATFORM_WINDOWS

extern Blinky::Application* Blinky::CreateApplication();

int main(int argc, char ** argv)
{
	auto app = Blinky::CreateApplication();
	app->Run();
	delete app;
}

#endif