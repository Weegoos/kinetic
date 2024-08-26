<template>
  <div>
    <q-layout view="lHr LpR lFf" container style="height: 100vh">
      <q-header reveal elevated bordered class="bg-white">
        <q-toolbar class="bg-white text-black">
          <q-btn flat round dense icon="menu" @click="drawer != drawer" />
        </q-toolbar>
      </q-header>
      <q-drawer
        side="left"
        v-model="drawer"
        bordered
        :width="250"
        :breakpoint="500"
        class="drawer text-white"
      >
        <div align="center" class="drawerIcon">
          <img src="../assets/general/logo.png" alt="" />
          <p class="text-white text-h5 text-bold">Kinetic</p>
        </div>
        <div>
          <q-list @click="pushToMainPage">
            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="home" />
              </q-item-section>
              <q-item-section>Главная страница</q-item-section>
            </q-item>
          </q-list>
        </div>
        <div>
          <q-tree
            :nodes="simple"
            dense
            dark
            node-key="label"
            v-model:expanded="expanded"
            class="tree text-white q-ml-md"
            default-expand-all
          >
          </q-tree>
        </div>
        <div>
          <q-list>
            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="code" />
              </q-item-section>
              <q-item-section>Аналитика</q-item-section>
            </q-item>
          </q-list>
        </div>
        <q-list>
          <q-item clickable v-ripple @click="pustToResultPage">
            <q-item-section avatar>
              <q-icon name="code" />
            </q-item-section>
            <q-item-section>Мои результаты</q-item-section>
          </q-item>
        </q-list>
      </q-drawer>
      <q-page-container>
        <q-page>
          <router-view />
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script setup>
import { useQuasar } from "quasar";
import { ref } from "vue";
import { useRouter } from "vue-router";
import calendar from "../assets/drawer/calendar.png";
const expanded = ref([]);
const router = useRouter();
const $q = useQuasar();
const simple = [
  {
    label: "Календарь",
    icon: "person",
    children: [
      {
        label: "Зачеты",
        handler: () => {
          router.push("/class_calendar");
        },
      },
      {
        label: "Мероприятия",
        handler: () => {
          router.push("/event_calendar");
        },
      },
    ],
  },
];

const drawer = ref(true);

const pushToMainPage = () => {
  router.push("/");
};

const pustToResultPage = () => {
  router.push("/result");
};
</script>

<style scoped>
.tree {
  color: white;
}
</style>
