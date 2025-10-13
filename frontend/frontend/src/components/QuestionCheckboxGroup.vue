<template>
    <div class="mb-10">
      <h2 class="font-semibold text-gray-800 mb-2">
        {{ number }}. {{ title }}
        <span v-if="required" class="text-red-500">*</span>
      </h2>
      <p v-if="subtitle" class="text-sm text-gray-500 mb-3">{{ subtitle }}</p>
  
      <div class="space-y-2">
        <label
          v-for="(option, index) in options"
          :key="index"
          class="flex items-start gap-2 text-sm text-gray-700"
        >
          <input
            type="checkbox"
            class="mt-1 accent-blue-600 w-4 h-4 cursor-pointer"
            :value="option"
            v-model="model"
          />
          <span>{{ option }}</span>
        </label>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    modelValue: Array,
    number: Number,
    title: String,
    subtitle: String,
    options: Array,
    required: Boolean
  })
  
  const emit = defineEmits(['update:modelValue'])
  
  const model = computed({
    get: () => props.modelValue,
    set: val => emit('update:modelValue', val)
  })
  </script>
  