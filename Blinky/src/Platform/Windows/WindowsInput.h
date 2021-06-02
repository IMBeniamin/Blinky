#pragma once
#include "Blinky/Input.h"

namespace Blinky
{
	class WindowInput : public Input
	{
	protected:
		virtual bool IsKeyPressedImpl(int keycode);

		bool IsMouseButtonPressedImpl(int button) override;
		virtual std::pair<float, float> GetMousePositionImpl() override;
		float GetMouseXImpl() override;
		float GetMouseYImpl() override;

	};
}