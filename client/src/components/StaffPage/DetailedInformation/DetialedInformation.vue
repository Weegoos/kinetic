<template>
  <div>
    <q-dialog v-model="openDetailedInformationWindow" persistent>
      <q-card style="width: 100vw">
        <q-tabs
          v-model="tab"
          dense
          class="bg-grey-2 text-grey-7"
          active-color="black"
          indicator-color="black"
          align="justify"
        >
          <q-tab name="physicalTraining" label="Физ. подготовка" />
          <q-tab name="alarms" label="Alarms" />
          <q-tab name="movies" label="Movies" />
          <q-btn icon="close" flat @click="closeDetailedInformationWindow" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="physicalTraining">
            Здесь будет физическая подготовка каждого сотрудника
          </q-tab-panel>

          <q-tab-panel name="alarms">
            <div class="text-h6">Alarms</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>

          <q-tab-panel name="movies">
            <div class="text-h6">Movies</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </q-dialog>
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
const tab = ref("physicalTraining");
const emit = defineEmits(["close"]);
const closeDetailedInformationWindow = () => {
  openDetailedInformationWindow.value = false;
  emit("close");
};
</script>
