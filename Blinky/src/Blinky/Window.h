#pragma once
#include "blpch.h"

#include "Blinky/Core/Base.h"
#include "Blinky/Events/Event.h"

namespace Blinky
{
	struct WindowProps {
		std::string Title;
		unsigned int Width;
		unsigned int Height;

		WindowProps(const std::string& title = "Blinky Engine",
			unsigned int width = 800,
			unsigned int height = 600)
			: Title(title), Width(width), Height(height)
			{}
	};

	// Interface representing a desktop based operating system window
	class BLINKY_API Window
	{
	public:
		using EventCallbackFn = std::function<void(Event&)>;
		virtual ~Window() = default;

		virtual void OnUpdate() = 0;

		virtual unsigned int GetWidth() const = 0;
		virtual unsigned int GetHeight() const = 0;
		
		// Window attributes
		virtual void SetEventCallback(const EventCallbackFn& callback) = 0;
		virtual void SetVSync(bool enabled) = 0;
		virtual bool IsVSync() const = 0;

		virtual void* GetNativeWindow() const = 0;

		static Window* Create(const WindowProps& props = WindowProps());
	};
}
