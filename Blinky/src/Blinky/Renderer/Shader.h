#pragma once

#include <string>

namespace Hazel {

	class Shader
	{
	public:
		Shader(const std::string& vertexSrc, const std::string& fragmentSrc);
		virtual ~Shader() = 0;

		virtual void Bind() const = 0;
		virtual void Unbind() const = 0;
	private:
		uint32_t m_RendererID;
	};

}