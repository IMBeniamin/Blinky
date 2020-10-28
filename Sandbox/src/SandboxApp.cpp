#include "Blinky.h"

class Sandbox : public Blinky::Application
{
public:
	Sandbox()
	{
	
	};
	~Sandbox()
	{
	
	};
};

Blinky::Application* Blinky::CreateApplication()
{
	return new Sandbox();
}