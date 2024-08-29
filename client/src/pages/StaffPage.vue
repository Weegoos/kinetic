<template>
  <div class="q-pa-md">
    <p class="text-bold text-h6">Поиск сотрудников</p>
    <section>
      <q-table flat bordered dense :rows="rows" :columns="columns" row-key="id">
        <template v-slot:body-cell-actions="props">
          <q-td :props="props">
            <q-btn flat size="sm" icon="edit" @click="editRow(props.row)">
              <q-tooltip> Редактировать </q-tooltip></q-btn
            >
            <q-btn
              flat
              size="sm"
              icon="menu"
              @click="openDetialedWindow(props.row)"
              class="q-ml-sm"
            >
              <q-tooltip> Подробнее </q-tooltip>
            </q-btn>
          </q-td>
        </template>
      </q-table>
      <DetialedInformation
        :openDetailedInformation="openDetailedInformation"
        @close="closeDetialedWindow"
      />
    </section>
  </div>
</template>

<script setup>
import { useQuasar } from "quasar";
import DetialedInformation from "../components/StaffPage/DetailedInformation/DetialedInformation.vue";
import axios from "axios";
import { onMounted, ref } from "vue";
import { getCurrentInstance } from "vue";
const { proxy } = getCurrentInstance();
const apiBaseUrl = proxy.$apiBaseUrl;
const getCookie = proxy.$getCookie;

const props = defineProps({
  getCorrectMessage: Function,
  // getIncorrectMessage: Function,
});
const $q = useQuasar();

onMounted(() => {
  console.log(apiBaseUrl);
  fetchAllUsers();
});

const fetchAllUsers = async () => {
  const token = getCookie("access_token");
  if (!token) {
    console.error("No access token found");
    $q.notify({
      message: "No access token found",
      color: "negative",
      position: "top",
    });
    return;
  }
  try {
    const response = await axios.get("https://kinetic.kz/api/users", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    props.getCorrectMessage("Данные успешно получены");

    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

const columns = [
  {
    name: "id",
    required: true,
    label: "№",
    field: "id",
    align: "left",
    sortable: true,
  },
  {
    name: "fullname",
    align: "center",
    label: "ФИО",
    field: "fullname",
    sortable: true,
  },
  {
    name: "physicalTraining",
    label: "Физ. подготовка",
    field: "physicalTraining",
    align: "center",
    sortable: true,
    sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "iin",
    label: "ИИН",
    field: "iin",
    align: "center",
    sortable: true,
    sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "department",
    label: "Управление",
    align: "center",
    field: "department",
    sortable: true,
  },
  {
    name: "specialty",
    label: "Специальность",
    field: "specialty",
    sortable: true,
  },
  // Add a column for actions
  {
    name: "actions",
    label: "Действия",
    align: "center",
  },
];

const rows = [
  {
    id: 1,
    fullname: "Иванов Иван Иванович",
    iin: "123456789012",
    department: "Управление 1",
    specialty: "Специалист",
    physicalTraining: "Хорошая",
  },
];

function editRow(row) {
  console.log("Editing row:", row);
}

const openDetailedInformation = ref(false);

function openDetialedWindow(row) {
  openDetailedInformation.value = true;
}

const closeDetialedWindow = () => {
  openDetailedInformation.value = false;
};
</script>

<style></style>
