document.addEventListener('DOMContentLoaded', function () {
    const data_topic = JSON.parse(document.getElementById("data_topic").getAttribute("data-var"));
    const socket = new WebSocket(
        'ws://' + window.location.host + '/mqtt/sensor/' + data_topic.topic + '/'
    );

    socket.onopen = function (e) {
        console.log("Conectado al WebSocket");
    };

    socket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const mqttData = JSON.parse(data.data_mqtt);
        console.log(mqttData);

        let factorVolts = 0.01
        let factorCurrent = 0.01
        let factorPower = 0.01
        let factorPowerCosen = 0.001

        document.getElementById('sensor').innerText = mqttData.sen;
        // Actualizar los valores de las cards
        document.getElementById('Va').innerText = (mqttData.Va * factorVolts).toFixed(2) + ' V';
        document.getElementById('Vb').innerText = (mqttData.Vb * factorVolts).toFixed(2) + ' V';
        document.getElementById('Vc').innerText = (mqttData.Vc * factorVolts).toFixed(2) + ' V';
        // Agrega más líneas según los datos MQTT que desees mostrar
        document.getElementById('Vab').innerText = (mqttData.Vab * factorVolts).toFixed(2) + ' V';
        document.getElementById('Vbc').innerText = (mqttData.Vbc * factorVolts).toFixed(2) + ' V';
        document.getElementById('Vca').innerText = (mqttData.Vca * factorVolts).toFixed(2) + ' V';
        // Agrega más líneas según los datos MQTT que desees mostrar
        document.getElementById('Ia').innerText = (mqttData.Ia * factorCurrent).toFixed(2) + ' A';
        document.getElementById('Ib').innerText = (mqttData.Ib * factorCurrent).toFixed(2) + ' A';
        document.getElementById('Ic').innerText = (mqttData.Ic * factorCurrent).toFixed(2) + ' A';
        // Agrega más líneas según los datos MQTT que desees mostrar
        document.getElementById('Pa').innerText = (mqttData.Pa * factorPower).toFixed(2) + ' Kw';
        document.getElementById('Pb').innerText = (mqttData.Pb * factorPower).toFixed(2) + ' Kw';
        document.getElementById('Pc').innerText = (mqttData.Pc * factorPower).toFixed(2) + ' Kw';
        // Agrega más líneas según los datos MQTT que desees mostrar
        document.getElementById('Energy').innerText = ((mqttData.Pa + mqttData.Pb + mqttData.Pc) * factorPower).toFixed(2) + ' Kw/h';
        document.getElementById('Fp').innerText = (mqttData.FP * factorPowerCosen).toFixed(2);
        document.getElementById('Hz').innerText = (mqttData.Hz * factorPower).toFixed(2) + ' Hz';
    };
});