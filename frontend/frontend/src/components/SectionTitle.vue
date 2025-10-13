<template>
    <div class="mb-8">
      <h1 class="text-2xl font-semibold text-gray-900">{{ title }}</h1>
      <p v-if="subtitle" class="text-blue-700 text-sm mt-2">{{ subtitle }}</p>
    </div>
  </template>
  
  <script setup>
  defineProps({
    title: String,
    subtitle: String,
  })
  </script>
  