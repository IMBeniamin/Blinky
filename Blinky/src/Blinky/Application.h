#pragma once

#include "Blinky/Core/Base.h"

#include "Window.h"
#include "Blinky/LayerStack.h"
#include "Blinky/Events/Event.h"
#include "Blinky/Events/ApplicationEvent.h"

#include "Blinky/ImGui/ImGuiLayer.h"

namespace Blinky {
	class BLINKY_API Application
	{
	public:
		Application();
		virtual ~Application();
		void Run();
		
		void OnEvent(Event& e);

		void PushLayer(Layer* layer);
		void PushOverlay(Layer* layer);

		inline Window& GetWindow() { return *m_Window; }

		inline static Application& Get() { return *s_Instance; }
	private:
		bool OnWindowClose(WindowCloseEvent& e);

		std::unique_ptr<Window> m_Window;
		ImGuiLayer* m_ImGuiLayer;
		bool m_Running = true;
		LayerStack m_LayerStack;

	private:
		static Application* s_Instance;
	};
	// to be defined in client
	Application* CreateApplication();
}

