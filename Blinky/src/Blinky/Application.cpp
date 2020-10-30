#include "Application.h"

#include "Blinky/Log.h"
#include "Blinky/Events/ApplicationEvent.h"

// TODO include other event types

namespace Blinky {
	Application::Application()
	{

	}
	Application::~Application()
	{

	}

	void Application::Run()
	{
		WindowResizeEvent e(1280, 720);
		BL_TRACE(e);
		while (true);
	}
}
