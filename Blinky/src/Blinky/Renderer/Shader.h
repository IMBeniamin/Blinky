#pragma once

#include <string>

namespace Blinky {

	class Shader
	{
	protected:
		Shader(std::string& src) { this->m_Src = src; };
	public:
		
		virtual ~Shader() = 0;

		virtual void Bind() const = 0;
		virtual void Unbind() const = 0;
	private:
		std::string m_Src;
	};

}