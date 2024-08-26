<template>
  <div class="demo-app">
    <div class="demo-app-main">
      <FullCalendar
        class="demo-app-calendar"
        :options="calendarOptions"
        ref="fullCalendarRef"
      >
        <template v-slot:eventContent="arg">
          <b>{{ arg.timeText }}</b>
          <i>{{ arg.event.title }}</i>
        </template>
      </FullCalendar>
    </div>

    <!-- q-dialog для ввода названия события -->
    <q-dialog v-model="dialogOpen" persistent>
      <q-card style="width: 400px">
        <q-card-section>
          <p class="text-h6 text-bold">Добавьте занятие в календарь</p>
          <span>Тип занятий</span>
          <q-input
            class="q-mb-sm"
            dense
            v-model="newEventType"
            autofocus
            autogrow
          />
          <span>Класс занятий</span>
          <q-input
            class="q-mb-sm"
            dense
            v-model="newEventClass"
            autofocus
            autogrow
          />
          <span>Время проведения</span>
          <q-input
            class="q-mb-sm"
            dense
            v-model="newEventTime"
            autofocus
            type="time"
          />
          <span>Место проведения</span>
          <q-input
            dense
            v-model="newEventLocation"
            type="text"
            autofocus
            autogrow
          />
        </q-card-section>
        <q-card-actions>
          <q-btn label="Отменить" @click="closeDialog" color="negative" />
          <q-btn label="Добавить" @click="saveEvent" color="green" />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <!-- q-dialog для подробной информации о занятий -->
    <q-dialog v-model="detailedInformation" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <span class="q-ml-sm text-bold text-h6"
            >Подробная информация о занятий</span
          >
        </q-card-section>
        <q-card-section class="q-ml-sm">
          <span>Тип занятия</span>
          <p class="detailedInfo">{{ detailedInformationTitle }}</p>
          <span>Класс занятия</span>
          <p class="detailedInfo">{{ detailedInformationClass }}</p>
          <span>Время проведения</span>
          <p class="detailedInfo">{{ detailedInformationTime }}</p>
          <span>Место проведения</span>
          <p class="detailedInfo">{{ detailedInformationLocation }}</p>
          <q-popup-edit
            v-model="editableLabel"
            :validate="(val) => val.length > 3"
            v-slot="scope"
          >
            <q-input
              autofocus
              dense
              v-model="scope.value"
              :rules="[(val) => scope.validate(val) || 'Требуется 3 символа']"
            >
              <template v-slot:after>
                <q-btn
                  flat
                  dense
                  color="negative"
                  icon="cancel"
                  @click.stop.prevent="scope.cancel"
                />
                <q-btn
                  flat
                  dense
                  color="positive"
                  icon="check_circle"
                  @click.stop.prevent="scope.set"
                  :disable="
                    scope.validate(scope.value) === false ||
                    scope.initialValue === scope.value
                  "
                />
              </template>
            </q-input>
          </q-popup-edit>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Закрыть" color="primary" v-close-popup />
          <q-btn
            flat
            label="Удалить занятие"
            color="negative"
            @click="removeEvent(currentClickInfo)"
            v-close-popup
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, nextTick } from "vue";
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import { INITIAL_EVENTS, createEventId } from "./event-utils";
import ruLocale from "@fullcalendar/core/locales/ru";
import { useQuasar } from "quasar";

const $q = useQuasar();
const fullCalendarRef = ref(null);
const calendarOptions = reactive({
  plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
  headerToolbar: {
    left: "prev,next today",
    center: "title",
    right: "dayGridMonth,timeGridWeek,timeGridDay",
  },
  initialView: "dayGridMonth",
  initialEvents: INITIAL_EVENTS,
  editable: true,
  selectable: true,
  selectMirror: true,
  dayMaxEvents: true,
  weekends: true,
  locale: ruLocale,
  select: handleDateSelect,
  eventClick: handleEventClick,
  eventsSet: handleEvents,
});
const editableLabel = ref("");
const currentEvents = ref([]);
const dialogOpen = ref(false);
const detailedInformation = ref(false);
const newEventType = ref("");
const newEventTime = ref("");
const newEventLocation = ref("");
const newEventClass = ref("");
const selectedDate = ref({});

const clearInput = () => {
  newEventType.value = "";
  newEventTime.value = "";
  newEventLocation.value = "";
};

function handleWeekendsToggle() {
  calendarOptions.weekends = !calendarOptions.weekends;
}

function handleDateSelect(selectInfo) {
  selectedDate.value = {
    start: selectInfo.startStr,
    end: selectInfo.endStr,
    allDay: selectInfo.allDay,
  };
  dialogOpen.value = true;
}

async function saveEvent() {
  await nextTick();
  const calendarApi = fullCalendarRef.value.getApi();
  if (newEventType.value && newEventTime.value) {
    const startDateTime = `${selectedDate.value.start.split("T")[0]}T${
      newEventTime.value
    }`;

    calendarApi.addEvent({
      id: createEventId(),
      title: newEventType.value,
      start: startDateTime,
      end: selectedDate.value.end,
      allDay: selectedDate.value.allDay,
      extendedProps: {
        eventTime: newEventTime.value,
        location: newEventLocation.value,
        class: newEventClass.value,
      },
    });
  }
  closeDialog();
  clearInput();
}

function closeDialog() {
  dialogOpen.value = false;
  clearInput();
}

const detailedInformationTitle = ref("");
const detailedInformationTime = ref("");
const detailedInformationLocation = ref("");
const detailedInformationClass = ref("");
const currentClickInfo = ref(null);

function handleEventClick(clickInfo) {
  detailedInformation.value = true;
  detailedInformationTitle.value = clickInfo.event.title;

  const eventTime = clickInfo.event.extendedProps.eventTime;
  const eventLocation = clickInfo.event.extendedProps.location;
  const eventClass = clickInfo.event.extendedProps.class;

  detailedInformationTime.value = eventTime;
  detailedInformationLocation.value = eventLocation;
  detailedInformationClass.value = eventClass;
  currentClickInfo.value = clickInfo;
}

function removeEvent(clickInfo) {
  if (currentClickInfo.value) {
    currentClickInfo.value.event.remove();
  }
}

function handleEvents(events) {
  currentEvents.value = events;
}
</script>

<style lang="css" scoped>
h2 {
  margin: 0;
  font-size: 16px;
}

ul {
  margin: 0;
  padding: 0 0 0 1.5em;
}

li {
  margin: 1.5em 0;
  padding: 0;
}

b {
  margin-right: 3px;
}

.demo-app {
  display: flex;
  min-height: 100%;
  font-size: 14px;
}

.demo-app-sidebar {
  width: 300px;
  line-height: 1.5;
  background: #eaf9ff;
  border-right: 1px solid #d3e2e8;
}

.demo-app-sidebar-section {
  padding: 2em;
}

.demo-app-main {
  flex-grow: 1;
  padding: 3em;
}

.fc {
  max-width: 1100px;
  margin: 0 auto;
}

.detailedInfo {
  background-color: #f5f5f5;
  padding: 5px;
  border-radius: 5px;
}
</style>
