#include "Blinky.h"

#include "imgui/imgui.h"

class TestLayer : public Blinky::Layer {
public:
	TestLayer(const std::string name= "Test")
		:Layer(name)
	{
		
	}

	void OnUpdate() override
	{
		//BL_INFO("TestLayer::Update");
	}

	virtual void OnImGuiRender() override
	{
		ImGui::Begin("Test");
		ImGui::Text("Hello World");
		ImGui::End();
	}

	void OnEvent(Blinky::Event& event) override
	{
		if (event.GetEventType() != Blinky::EventType::AppTick)
			BL_INFO("{0}", event);
	}

};

class Sandbox : public Blinky::Application
{
public:
	Sandbox()
	{
		PushLayer(new TestLayer());
	};
	~Sandbox()
	{
		
	};
};

Blinky::Application* Blinky::CreateApplication()
{
	return new Sandbox();
}
