<template>
    <div class="mb-10">
      <h2 class="font-semibold text-gray-800 mb-2">
        {{ number }}. {{ title }}
        <span v-if="required" class="text-red-500">*</span>
      </h2>
      <p v-if="subtitle" class="text-sm text-gray-500 mb-3">{{ subtitle }}</p>
  
      <textarea
        v-model="model"
        :placeholder="placeholder"
        rows="3"
        class="w-full border border-gray-300 rounded-lg px-4 py-3 text-sm focus:ring-2 focus:ring-blue-400 outline-none resize-none"
      ></textarea>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    modelValue: String,
    number: Number,
    title: String,
    subtitle: String,
    placeholder: String,
    required: Boolean,
  })
  
  const emit = defineEmits(['update:modelValue'])
  
  const model = computed({
    get: () => props.modelValue,
    set: val => emit('update:modelValue', val)
  })
  </script>
  