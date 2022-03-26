﻿#pragma once

#include <memory>

namespace Blinky
{
	class VertexBuffer
	{
	public:
		virtual ~VertexBuffer();

		virtual void Bind() const = 0;
		virtual void Unbind() const = 0;

		static VertexBuffer* Create(std::unique_ptr<float> vertices, uint32_t size);
	};

	class IndexBuffer
	{
	public:
		virtual ~IndexBuffer() {}

		virtual void Bind() const = 0;
		virtual void Unbind() const = 0;

		virtual uint32_t GetCount() const = 0;

		static IndexBuffer* Create(std::unique_ptr< uint32_t> indices, uint32_t size);
	};
}