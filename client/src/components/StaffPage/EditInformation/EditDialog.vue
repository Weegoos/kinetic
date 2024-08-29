<template>
  <div>
    <q-dialog v-model="confirmEditDialog" persistent>
      <q-card>
        <q-card-section>
          Здесь будут поля для изменение физических данных сотрудника
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  openEditDialogInformation: {
    type: Boolean,
    required: true,
  },
});

const confirmEditDialog = ref(props.openEditDialogInformation);
watch(
  () => props.openEditDialogInformation,
  (newVal) => {
    confirmEditDialog.value = newVal;
  }
);

const emit = defineEmits(["close"]);
const closeDialog = () => {
  emit("close");
};
</script>

<style></style>
