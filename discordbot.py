import selfcore from "selfcore";

const client = new selfcore();
const gateway = new selfcore.Gateway(
  "Mzg3MjYxNzI4NjI0MzQ1MDg5.Ym6xTg.XsgJHPl5V8Bbp3F7hQ_1tz2iQYQ"
);

gateway.on("message", (m) => {
  if (m.channel_id === "931341731016867900") {
    let content = m.content ? m.content : { embeds: [m.embeds[0]] };

    client.sendWebhook(
      "https://discord.com/api/webhooks/1011248751979008071/uzAxemti9YpMb6nFhSOxZ0cTbz7nekvpgKEjQ0q_5HjzZU3MqoazA4qqAR4z3pqAECcU",
      content
    );
  }
});
