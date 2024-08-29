// src/boot/config.js
export default ({ app, $q }) => {
  // Объявляем глобальные переменные
  const apiBaseUrl = "http://localhost:8000/api/"; // Основной API URL
  const mockBaseUrl = "http://localhost:8001/"; // URL для mock-сервера

  // getcookie
  const getCookie = (name) => {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      const cookieValue = parts.pop().split(";").shift();
      console.log(`Cookie found: ${name}=${cookieValue}`);
      return cookieValue;
    }
    console.log(`Cookie not found: ${name}`);
    return null;
  };
  // Регистрация переменных как глобальных свойств
  app.config.globalProperties.$apiBaseUrl = apiBaseUrl;
  app.config.globalProperties.$mockBaseUrl = mockBaseUrl;
  app.config.globalProperties.$getCookie = getCookie;
};
