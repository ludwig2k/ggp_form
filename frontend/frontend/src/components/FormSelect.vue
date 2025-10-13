<template>
    <div>
      <label class="block mb-1 text-sm font-medium text-gray-700">{{ label }}</label>
      <select
        v-model="model"
        class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 outline-none"
      >
        <option value="" disabled selected hidden>{{ placeholder }}</option>
        <option v-for="(option, index) in options" :key="index" :value="option.value">
          {{ option.label }}
        </option>
      </select>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    modelValue: String,
    label: String,
    placeholder: String,
    options: { type: Array, default: () => [] }
  })
  
  const emit = defineEmits(['update:modelValue'])
  
  const model = computed({
    get: () => props.modelValue,
    set: val => emit('update:modelValue', val)
  })
  </script>
  