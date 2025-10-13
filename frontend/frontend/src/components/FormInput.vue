<template>
    <div>
      <label class="block mb-1 text-sm font-medium text-gray-700">{{ label }}</label>
      <input
        v-model="model"
        :type="type"
        :placeholder="placeholder"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 outline-none"
      />
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    modelValue: String,
    label: String,
    type: { type: String, default: 'text' },
    placeholder: String
  })
  
  const emit = defineEmits(['update:modelValue'])
  
  const model = computed({
    get: () => props.modelValue,
    set: val => emit('update:modelValue', val)
  })
  </script>
  