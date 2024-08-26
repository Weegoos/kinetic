<template>
  <div class="q-ma-md">
    <p class="text-bold text-h6">Аналитика</p>
    <section class="row q-gutter-md">
      <div class="col">
        <q-card class="my-card">
          <q-input
            class="input"
            v-model="time"
            type="text"
            label="Временные рамки"
            dense
          />
        </q-card>
      </div>
      <div class="col">
        <q-card class="my-card">
          <q-input
            class="input"
            v-model="people"
            type="text"
            label="Люди"
            dense
          />
        </q-card>
      </div>
      <div class="col">
        <q-card class="my-card">
          <q-input
            class="input"
            v-model="exercises"
            type="text"
            label="Упражнение"
            dense
          />
        </q-card>
      </div>
    </section>

    <section class="q-mt-md">
      <div class="row q-gutter-md">
        <div class="col analytics">
          <GeneralAnalytics />
        </div>
        <div class="col">Batyr</div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue";
import GeneralAnalytics from "../components/Analytics/GeneralAnalytics.vue";
const time = ref("");
const people = ref("");
const exercises = ref("");
</script>

<style scoped>
.input {
  padding: 8px;
}
</style>
