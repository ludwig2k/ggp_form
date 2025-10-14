<template>
  <div class="form-wide mx-auto bg-white p-8 lg:p-16 rounded-2xl shadow-lg">

    <SectionTitle
      title="Entendendo demandas técnicas e de informação / conhecimento"
      subtitle="Quais suas dúvidas ou dificuldades em relação aos tópicos abaixo:"
    />

    <QuestionCheckboxGroup
      v-model="form.ferias"
      :number="1"
      title="Solicitação e gestão de Férias"
      subtitle="Selecione no máximo 3 opções."
      :options="[
        'Dúvidas legais',
        'Dificuldades com prazos',
        'Gestão da equipe (ex: todos querem tirar ao mesmo tempo)',
        'Outra dúvida',
        'Não possuo dúvida ou dificuldade'
      ]"
      required
    />

    <QuestionTextarea
      v-model="form.outraFerias"
      :number="2"
      title="Outra dúvida não citada?"
      subtitle="Sobre solicitação e gestão de férias"
      placeholder="Insira sua resposta"
    />

    <QuestionCheckboxGroup
      v-model="form.ponto"
      :number="3"
      title="Gestão da frequência e ponto eletrônico"
      subtitle="Selecione no máximo 3 opções."
      :options="[
        'Sobre grades de horário',
        'Dúvidas sobre banco de horas e compensação',
        'Problemas com gestão da equipe (ex: não sei o que posso ou não justificar)',
        'Outras dúvidas',
        'Não possuo dúvida ou dificuldade'
      ]"
      required
    />
    <!-- 4 -->
<QuestionTextarea
  v-model="form.outraPonto"
  :number="4"
  title="Outra dúvida não citada?"
  subtitle="Sobre gestão da frequência e ponto eletrônico"
  placeholder="Insira sua resposta"
/>

<!-- 5 -->
<QuestionCheckboxGroup
  v-model="form.gratificacoes"
  :number="5"
  title="Gestão e concessão de gratificações"
  subtitle="Selecione no máximo 3 opções."
  :options="[
    'Dúvidas gerais',
    'Quem faz a gestão dos benefícios (onde posso conseguir uma gratificação)',
    'Problemas com gestão na equipe (ex: não sei o que medir para atribuir)',
    'Outra dúvida',
    'Não possuo dúvida ou dificuldade'
  ]"
  required
/>

<!-- 6 -->
<QuestionTextarea
  v-model="form.outraGratificacoes"
  :number="6"
  title="Outra dúvida não citada?"
  subtitle="Sobre gestão e concessão de gratificações"
  placeholder="Insira sua resposta"
/>

<!-- 7 -->
<QuestionCheckboxGroup
  v-model="form.atestados"
  :number="7"
  title="Atestados e Afastamentos"
  subtitle="Selecione no máximo 3 opções."
  :options="[
    'Dúvidas gerais',
    'Dificuldade/Dúvida com prazos de lançamento e/ou entrega de atestados',
    'Problemas com gestão na equipe (Ex: muitos afastamentos)',
    'Outra dúvida',
    'Não possuo dúvida ou dificuldade'
  ]"
  required
/>

<!-- 8 -->
<QuestionTextarea
  v-model="form.outraAtestados"
  :number="8"
  title="Outra dúvida não citada?"
  subtitle="Sobre atestados e afastamentos"
  placeholder="Insira sua resposta"
/>

<!-- 9 -->
<QuestionCheckboxGroup
  v-model="form.licencas"
  :number="9"
  title="Concessão de Licenças Variadas"
  subtitle="Seja licença prêmio, capacitação, para interesses particulares ou alguma outra. Selecione no máximo 3 opções."
  :options="[
    'Dúvidas gerais',
    'Quem aprova a concessão de licenças',
    'Dificuldade/Dúvida com prazos',
    'Dificuldade de gestão (Ex: pessoas não comunicam com antecedência ou não há programação da equipe)',
    'Outra dúvida',
    'Não possuo dúvida ou dificuldade'
  ]"
  required
/>

<!-- 10 -->
<QuestionTextarea
  v-model="form.outraLicencas"
  :number="10"
  title="Outra dúvida não citada?"
  subtitle="Sobre concessão de licenças variadas"
  placeholder="Insira sua resposta"
/>

<!-- 15 -->
<QuestionCheckboxGroup
  v-model="form.aposentadoria"
  :number="11"
  title="Solicitação de Aposentadoria"
  subtitle="Selecione no máximo 3 opções."
  :options="[
    'Dúvidas quanto ao planejamento para aposentadoria',
    'Quanto a normas legais como prazos e alíquotas',
    'Tempo de duração do meu processo',
    'Não possuo dúvida ou dificuldade'
  ]"
  required
/>

<!-- After aposentadoria checkbox group -->
<QuestionTextarea
  v-model="form.outraAposentadoria"
  :number="12"
  title="Outra dúvida não citada?"
  subtitle="Sobre solicitação de aposentadoria"
  placeholder="Insira sua resposta"
/>

<!-- 16 -->
<QuestionCheckboxGroup
  v-model="form.folhaPagamento"
  :number="12"
  title="Folha de pagamento e descontos"
  subtitle="Selecione no máximo 3 opções."
  :options="[
    'Quando acontecem os descontos',
    'Prazos de fechamento de folha e o que isso impacta',
    'Visualização do contracheque',
    'Outra dúvida',
    'Não possuo dúvida ou dificuldade'
  ]"
  required
/>

<!-- After folhaPagamento checkbox group -->
<QuestionTextarea
  v-model="form.outraFolhaPagamento"
  :number="13"
  title="Outra dúvida não citada?"
  subtitle="Sobre folha de pagamento e descontos"
  placeholder="Insira sua resposta"
/>

<!-- 11 -->
<div class="mb-10">
  <h2 class="font-semibold text-gray-800 mb-2">
    13. Você sabe o que fazer quando precisa de um servidor a mais na equipe?
    <span class="text-red-500">*</span>
  </h2>
  <div class="space-y-2">
    <label class="flex items-center gap-2 text-sm text-gray-700">
      <input type="radio" value="Sim" v-model="form.servidorExtra" class="accent-blue-600 w-4 h-4 cursor-pointer" />
      <span>Sim</span>
    </label>
    <label class="flex items-center gap-2 text-sm text-gray-700">
      <input type="radio" value="Não" v-model="form.servidorExtra" class="accent-blue-600 w-4 h-4 cursor-pointer" />
      <span>Não</span>
    </label>
  </div>
</div>

<!-- 12 -->
<QuestionTextarea
  v-model="form.duvidaServidorExtra"
  :number="14"
  title="Caso não para a pergunta anterior, qual a sua dúvida?"
  placeholder="Insira sua resposta"
/>

<!-- 13 -->
<div class="mb-10">
  <h2 class="font-semibold text-gray-800 mb-2">
    15. Você sabe o que fazer quando precisa desligar um servidor?
    <span class="text-red-500">*</span>
  </h2>
  <div class="space-y-2">
    <label class="flex items-center gap-2 text-sm text-gray-700">
      <input type="radio" value="Sim" v-model="form.desligarServidor" class="accent-blue-600 w-4 h-4 cursor-pointer" />
      <span>Sim</span>
    </label>
    <label class="flex items-center gap-2 text-sm text-gray-700">
      <input type="radio" value="Não" v-model="form.desligarServidor" class="accent-blue-600 w-4 h-4 cursor-pointer" />
      <span>Não</span>
    </label>
  </div>
</div>

<!-- 14 -->
<QuestionTextarea
  v-model="form.duvidaDesligarServidor"
  :number="16"
  title="Caso não para a pergunta anterior, qual a sua dúvida?"
  placeholder="Insira sua resposta"
/>


<!-- Section title -->
<div class="mt-12 mb-4">
  <h2 class="text-xl font-bold text-blue-800">Alinhando Expectativas</h2>
  <p class="text-gray-600 text-sm mt-1">
    Nos ajude a entender as suas demandas e necessidades.
  </p>
</div>

<!-- 15 -->
<QuestionCheckboxGroup
  v-model="form.esperaGGDP"
  :number="17"
  title="O que você espera da GGDP?"
  subtitle="Na sua visão, qual o nosso papel (ou qual deveria ser) na SEAD e na sua liderança?"
  :options="[
    'Cumprir normas e procedimentos burocráticos',
    'Controlar toda a folha de pagamento e frequência dos servidores da SEAD',
    'Ajudar a criar indicadores nas diversas áreas',
    'Comunicar exoneração para os servidores',
    'Escutar os servidores',
    'Escutar as lideranças',
    'Treinar e desenvolver pessoas'
  ]"
/>

<!-- 16 -->
<QuestionTextarea
  v-model="form.justificativaGGDP"
  :number="18"
  title="Sobre a pergunta anterior, justifique sua resposta e/ou nos conte qual outra competência que não foi citada:"
  placeholder="Insira sua resposta"
  required
/>

<!-- 17 -->
<QuestionTextarea
  v-model="form.melhorias"
  :number="19"
  title="Nos conte algo que podemos melhorar que impactará positivamente na gestão da sua equipe!"
  subtitle="Esse é um campo feito para melhorarmos nossa atuação, e te ajudarmos na sua gestão!"
  placeholder="Insira sua resposta"
  required
/>


    <!-- === Submit Button + Modal === -->
    <div class="pt-6 border-t mt-8">
      <button
        @click="openNameModal"
        :disabled="submitting"
        class="bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
      >
        {{ submitting ? 'Enviando...' : 'Enviar respostas' }}
      </button>

      <p v-if="success" class="text-green-600 mt-3">✅ Respostas enviadas com sucesso!</p>
      <p v-if="error" class="text-red-600 mt-3">{{ error }}</p>
    </div>

    <!-- Modal for name -->
    <div
      v-if="showNameModal"
      class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-xl p-8 w-full max-w-md shadow-lg text-center">
        <h2 class="text-xl font-semibold text-gray-800 mb-4">Antes de enviar...</h2>
        <p class="text-gray-600 mb-4">
          Por favor, digite seu nome para registrar sua resposta:
        </p>

        <input
          v-model="userName"
          @keyup.enter="submitWithName"
          type="text"
          placeholder="Seu nome completo"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none mb-6"
        />

        <div class="flex justify-center gap-4">
          <button
            @click="submitWithName"
            :disabled="!userName.trim()"
            class="bg-blue-600 text-white px-5 py-2 rounded-lg font-medium hover:bg-blue-700 transition disabled:opacity-50"
          >
            Confirmar
          </button>
          <button
            @click="showNameModal = false"
            class="bg-gray-300 text-gray-700 px-5 py-2 rounded-lg font-medium hover:bg-gray-400 transition"
          >
            Cancelar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import SectionTitle from './SectionTitle.vue'
import QuestionCheckboxGroup from './QuestionCheckboxGroup.vue'
import QuestionTextarea from './QuestionTextarea.vue'

const form = ref({
  ferias: [],
  outraFerias: '',
  ponto: [],
  outraPonto: '',
  gratificacoes: [],
  outraGratificacoes: '',
  atestados: [],
  outraAtestados: '',
  licencas: [],
  outraLicencas: '',
  servidorExtra: '',
  duvidaServidorExtra: '',
  desligarServidor: '',
  duvidaDesligarServidor: '',
  esperaGGDP: [],
  justificativaGGDP: '',
  melhorias: '',
  nome: '',
  aposentadoria: [],
  folhaPagamento: [],
  outraAposentadoria: '',
  outraFolhaPagamento: ''
})

const submitting = ref(false)
const success = ref(false)
const error = ref('')
const showNameModal = ref(false)
const userName = ref('')

const openNameModal = () => (showNameModal.value = true)

const submitWithName = async () => {
  showNameModal.value = false
  form.value.nome = userName.value

  submitting.value = true
  success.value = false
  error.value = ''

  try {
    const res = await axios.post('http://127.0.0.1:5000/api/form', form.value)
    console.log('Resposta do servidor:', res.data)
    success.value = true
    userName.value = ''
  } catch (err) {
    console.error(err)
    error.value = 'Ocorreu um erro ao enviar o formulário.'
  } finally {
    submitting.value = false
  }
}
</script>
<style scoped>
/* Main container */
.form-wide {
  width: 95%;
  max-width: 1800px !important;
  margin: 2rem auto;
  min-height: calc(100vh - 200px);
  padding: 3rem !important;
}

/* Question blocks and spacing */
:deep(.question-block) {
  background-color: #f8fafc;
  border-radius: 1rem;
  padding: 2rem !important;
  margin-bottom: 3rem !important;
  border: 1px solid #e2e8f0;
}

/* Question titles */
:deep(h2) {
  font-size: 1.25rem !important;
  font-weight: 600 !important;
  color: #1e40af !important;
  margin-bottom: 1rem !important;
  line-height: 1.4 !important;
}

/* Subtitles and labels */
:deep(p), 
:deep(label) {
  font-size: 1rem !important;
  color: #4b5563 !important;
  margin-bottom: 1rem !important;
  line-height: 1.5 !important;
}

/* Checkbox and radio groups */
:deep(.space-y-2) {
  display: flex;
  flex-direction: column;
  gap: 1rem !important;
  margin-top: 1.5rem !important;
}

/* Individual checkbox/radio items */
:deep(input[type="checkbox"]),
:deep(input[type="radio"]) {
  width: 1.25rem !important;
  height: 1.25rem !important;
  margin-right: 0.75rem !important;
}

/* Checkbox/radio labels */
:deep(input[type="checkbox"] + span),
:deep(input[type="radio"] + span) {
  font-size: 1rem !important;
  color: #374151 !important;
}

/* Textarea fields */
:deep(textarea) {
  width: 100% !important;
  min-height: 120px !important;
  padding: 1rem !important;
  margin-top: 1rem !important;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  background-color: white;
}

/* Required field asterisk */
:deep(.text-red-500) {
  margin-left: 0.25rem;
}

/* Section margins */
:deep(.mb-10) {
  margin-bottom: 4rem !important;
}
</style>