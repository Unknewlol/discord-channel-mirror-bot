import selfcore from "selfcore";

const client = new selfcore();
const gateway = new selfcore.Gateway(
  "OTA4OTkzODYwNTg2MzE1Nzc2.GpqaSi._1yE3gqymMJgtUnymLWR7GNzSCoDiB5lm1FmVc"
);

gateway.on("message", (m) => {
  if (m.channel_id === "941753577758654485") {
    let content = m.content ? m.content : { embeds: [m.embeds[0]] };

    client.sendWebhook(
      "https://discord.com/api/webhooks/1021779952883994624/g_ilP0pVrLwoPFJ-yv5wk9lqErfQbAwvc6yoqh_2CYE4f7FCDKjoVI7QkkfryhJmRK99",
      content
    );
  }
});
