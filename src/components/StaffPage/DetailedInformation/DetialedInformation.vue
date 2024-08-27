<template>
  <div>
    <q-dialog v-model="openDetailedInformationWindow" persistent> </q-dialog>
  </div>
</template>

<script setup>
import { useQuasar } from "quasar";
import { ref, watch } from "vue";

const $q = useQuasar();
const props = defineProps({
  openDetailedInformation: {
    type: Boolean,
    required: true,
  },
});

const openDetailedInformationWindow = ref(props.openDetailedInformation);

watch(
  () => props.openDetailedInformation,
  (newVal) => {
    openDetailedInformationWindow.value = newVal;
  }
);

const emit = defineEmits(["close"]);
const closeDetailedInformationWindow = () => {
  openDetailedInformationWindow.value = false;
  emit("close");
};
</script>
