<template>
  <div>
    <q-dialog v-model="openWindow" persistent>
      <q-card class="my-card" style="width: 100vw">
        <q-card-section>
          <section class="row">
            <div class="col q-mt-sm">
              {{ props.chartName }}
            </div>
            <div class="col" align="right">
              <q-btn icon="close" flat @click="closeDialog" />
            </div>
          </section>
        </q-card-section>
        <q-list bordered>
          <q-item clickable v-ripple>
            <q-item-section></q-item-section>
          </q-item>
        </q-list>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  chartName: {
    type: String,
    required: true,
  },
  exercisesDialog: {
    type: Boolean,
    required: true,
  },
});

const openWindow = ref(props.exercisesDialog);

watch(
  () => props.exercisesDialog,
  (newVal) => {
    openWindow.value = newVal;
  }
);

const emit = defineEmits(["close"]);
const closeDialog = () => {
  emit("close");
};
</script>

<style></style>
