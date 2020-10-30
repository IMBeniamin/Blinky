#pragma once

#include "Blinky/Core.h"
#include "Blinky/Events/Event.h"

#include <sstream>

namespace Blinky {
	class BLINKY_API WindowEvent : public Event
	{
	protected:
		WindowEvent() {}
	public:
		EVENT_CLASS_CATEGORY(EventCategoryApplication)
		
	};

	class BLINKY_API AppEvent : public Event
	{
	protected:
		AppEvent() {}
	public:
		EVENT_CLASS_CATEGORY(EventCategoryApplication)

	};

	// WINDOW EVENTS

	class BLINKY_API WindowResizeEvent : public WindowEvent
	{
	public:
		WindowResizeEvent(unsigned int width, unsigned int height)
			: m_Width(width), m_Height(height) {}

		inline unsigned int GetWidth() const { return m_Width; }
		inline unsigned int GetHeight() const { return m_Height; }
		
		std::string ToString() const override
		{
			std::stringstream ss;
			ss << "WindowResizeEvent :" << m_Width << ", " << m_Height << std::endl;
			return ss.str();
		}

		EVENT_CLASS_TYPE(WindowResize)

	private:
		unsigned int m_Width, m_Height;
	};

	class BLINKY_API WindowCloseEvent : public WindowEvent
	{
	public:
		WindowCloseEvent() {}

		EVENT_CLASS_TYPE(WindowClose)
	};

	// APP EVENTS

	class BLINKY_API AppTickEvent : public AppEvent
	{
	public:
		AppTickEvent() {}

		EVENT_CLASS_TYPE(AppTick)
	};

	class BLINKY_API AppUpdateEvent : public AppEvent
	{
	public:
		AppUpdateEvent() {}

		EVENT_CLASS_TYPE(AppUpdate)
	};

	class BLINKY_API AppRenderEvent : public AppEvent
	{
	public:
		AppRenderEvent() {}

		EVENT_CLASS_TYPE(AppRender)
	};
}
