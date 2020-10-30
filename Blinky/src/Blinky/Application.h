#pragma once

#include "Core.h"
#include "Blinky/Events/Event.h"

namespace Blinky {
	class BLINKY_API Application
	{
	public:
		Application();
		virtual ~Application();
		void Run();
	};

	// to be defined in client
	Application* CreateApplication();
}

