#include "blpch.h"
#include "RenderCommand.h"

#include "Platform/OpenGL/OpenGLRendererAPI.h"

namespace Blinky {
	RendererAPI* RenderCommand::s_RendererAPI = new OpenGLRendererAPI;
}
