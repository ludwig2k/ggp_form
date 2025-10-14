<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Top navigation -->
    <header class="sticky top-0 z-10 flex justify-center gap-4 py-4 bg-blue-50 border-b border-blue-200 shadow-sm">
      <button
        @click="handleNavClick('form')"
        :class="[
          'px-5 py-2.5 rounded-lg font-medium transition-all duration-200',
          currentView === 'form'
            ? 'bg-blue-600 text-white shadow-md'
            : 'bg-white text-blue-600 border border-blue-400 hover:bg-blue-100'
        ]"
      >
        Formulário
      </button>

      <button
        @click="handleNavClick('admin')"
        :class="[
          'px-5 py-2.5 rounded-lg font-medium transition-all duration-200',
          currentView === 'admin'
            ? 'bg-blue-600 text-white shadow-md'
            : 'bg-white text-blue-600 border border-blue-400 hover:bg-blue-100'
        ]"
      >
        Admin
      </button>
    </header>

    <!-- Admin password modal -->
    <div
      v-if="showAdminModal"
      class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-xl p-8 w-full max-w-md shadow-lg">
        <h2 class="text-xl font-semibold text-gray-800 mb-4">Acesso Restrito</h2>
        <p class="text-gray-600 mb-4">Digite a senha para acessar a área administrativa:</p>

        <input
          v-model="adminPassword"
          @keyup.enter="checkAdminPassword"
          type="password"
          placeholder="Senha"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none mb-4"
        />

        <p v-if="adminError" class="text-red-500 text-sm mb-4">{{ adminError }}</p>

        <div class="flex justify-end gap-4">
          <button
            @click="closeAdminModal"
            class="px-4 py-2 text-gray-600 hover:text-gray-800"
          >
            Cancelar
          </button>
          <button
            @click="checkAdminPassword"
            class="bg-blue-600 text-white px-5 py-2 rounded-lg font-medium hover:bg-blue-700 transition"
          >
            Entrar
          </button>
        </div>
      </div>
    </div>

    <!-- Dynamic view -->
    <main class="flex-1 w-full py-8">
      <div class="w-full max-w-[90%] mx-auto">
        <FormContainer v-if="currentView === 'form'" />
        <AdminDashboard v-else />
      </div>
    </main>

    <!-- Footer -->
    <footer class="text-center text-sm text-gray-500 py-6 border-t">
      © {{ new Date().getFullYear() }} GGDP Form — built with Vue & Flask 💙
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import FormContainer from './components/FormContainer.vue'
import AdminDashboard from './components/AdminDashboard.vue'

const currentView = ref('form')
const showAdminModal = ref(false)
const adminPassword = ref('')
const adminError = ref('')

// Replace this with your desired admin password
const ADMIN_PASSWORD = 'lino'

const tryAccessAdmin = () => {
  adminPassword.value = ''
  adminError.value = ''
  showAdminModal.value = true
}

const closeAdminModal = () => {
  showAdminModal.value = false
  adminPassword.value = ''
  adminError.value = ''
}

const checkAdminPassword = () => {
  if (adminPassword.value === ADMIN_PASSWORD) {
    currentView.value = 'admin'
    closeAdminModal()
  } else {
    adminError.value = 'Senha incorreta'
    adminPassword.value = ''
  }
}

// Update the header button click handler
const handleNavClick = (view) => {
  if (view === 'admin') {
    tryAccessAdmin()
  } else {
    currentView.value = view
  }
}
</script>

<style>
/* --- Desktop expand: remove every common width limiter under .form-wide --- */
.form-wide .container,
.form-wide .prose,
.form-wide .mx-auto,
.form-wide .max-w-xs,
.form-wide .max-w-sm,
.form-wide .max-w-md,
.form-wide .max-w-lg,
.form-wide .max-w-xl,
.form-wide .max-w-2xl,
.form-wide .max-w-3xl,
.form-wide .max-w-4xl,
.form-wide .max-w-5xl,
.form-wide [class*="max-w-"] {
  max-width: none !important;
  width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
}

/* Some components use fixed pixel widths. Kill those too. */
.form-wide [style*="width:"],
.form-wide [style*="max-width:"] {
  max-width: none !important;
  width: 100% !important;
}

/* Make inner blocks actually use the space */
.form-wide .question-block,
.form-wide section,
.form-wide form,
.form-wide > * {
  width: 100% !important;
}
input[type="text"],
input[type="password"],
textarea {
  color: #374151 !important; /* gray-700 */
  background-color: white !important;
}

/* Ensure placeholder text is visible but slightly dimmed */
input::placeholder,
textarea::placeholder {
  color: #9CA3AF !important; /* gray-400 */
}

/* Ensure text remains visible when autofilled */
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
textarea:-webkit-autofill,
textarea:-webkit-autofill:hover,
textarea:-webkit-autofill:focus {
  -webkit-text-fill-color: #374151 !important;
  -webkit-box-shadow: 0 0 0px 1000px white inset;
  transition: background-color 5000s ease-in-out 0s;
}
</style>
