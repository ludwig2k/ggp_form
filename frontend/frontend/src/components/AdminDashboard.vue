<template>
    <div class="min-h-screen bg-gray-50 p-8">
      <h1 class="text-3xl font-bold text-blue-700 mb-8">Painel de Respostas</h1>
  
      <div v-if="loading" class="text-gray-600">Carregando respostas...</div>
      <div v-if="error" class="text-red-600">{{ error }}</div>
  
      <div v-if="responses.length" class="space-y-6">
        <div
          v-for="(resp, i) in responses"
          :key="resp.id"
          class="bg-white border border-gray-200 rounded-lg shadow-sm p-5"
        >
          <div
            class="flex justify-between items-center cursor-pointer"
            @click="toggleExpanded(i)"
          >
            <div>
              <h2 class="font-semibold text-gray-800 text-lg">
                {{ resp.user_name }}
              </h2>
              <p class="text-sm text-gray-500">
                {{ new Date(resp.created_at).toLocaleString('pt-BR') }}
              </p>
            </div>
            <button class="text-blue-600 hover:underline text-sm font-medium">
              {{ expanded[i] ? 'Fechar' : 'Ver detalhes' }}
            </button>
          </div>
  
          <div
            v-if="expanded[i]"
            class="mt-4 border-t pt-3 text-sm text-gray-700 whitespace-pre-wrap"
          >
            {{ formatData(resp.data) }}
          </div>
        </div>
      </div>
  
      <div v-if="!loading && !responses.length && !error" class="text-gray-500">
        Nenhuma resposta encontrada.
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const responses = ref([])
  const loading = ref(true)
  const error = ref('')
  const expanded = ref([])
  
  const toggleExpanded = (i) => {
    expanded.value[i] = !expanded.value[i]
  }
  
  const formatData = (data) => {
    return Object.entries(data)
      .map(([key, value]) => `${key}: ${Array.isArray(value) ? value.join(', ') : value}`)
      .join('\n')
  }
  
  onMounted(async () => {
    try {
      const res = await axios.get('http://127.0.0.1:5000/api/form/all')
      responses.value = res.data
      expanded.value = Array(responses.value.length).fill(false)
    } catch (err) {
      error.value = 'Erro ao carregar respostas.'
    } finally {
      loading.value = false
    }
  })
  </script>
  