# Jewish Date & Holiday & Shabbat Automation Rules

Reference data for scheduling home automations around Jewish holidays and Shabbat. Exact times are location-specific and should be pulled from the holiday data source (e.g. Hebcal) rather than hardcoded.

## Candle Lighting

Jewish holidays begin at sunset. Candle lighting occurs before sunset.

| Occasion | Timing |
|---|---|
| Regular Shabbat | 18 minutes before sunset |
| Yom Tov (holidays) | 18 minutes before sunset |
| Erev Yom Kippur | 20–40 minutes before sunset (varies by community) |

**Automation note:** Use the candle lighting time from the event data, not a fixed offset, since it is location-specific.

## Havdalah

Jewish holidays end at nightfall (when 3 stars are visible).

| Occasion | Timing |
|---|---|
| Shabbat ends | ~42–72 minutes after sunset (varies by community) |
| Yom Tov ends | ~42–72 minutes after sunset (varies by community) |

Havdalah is the ceremony marking the end of Shabbat or a holiday. The exact time is location-specific and provided in the holiday data.

## Yom Kippur

**Day of Atonement**

- **Begins:** Candle lighting time (typically 20–40 minutes before sunset on Erev Yom Kippur)
- **Ends:** Nightfall the next day (~42–72 minutes after sunset)
- **Duration:** ~25 hours of fasting and prayer

**Special considerations:**
- All work prohibited (like Shabbat)
- No eating or drinking
- Lights should be on timers before the holiday begins
- Consider pre-setting thermostats

**Automation rule:** Set candle lighting time 10–40 minutes before sunset on erev.

## Shabbat

**Sabbath**

- **Begins:** Friday at candle lighting (18 minutes before sunset)
- **Ends:** Saturday at nightfall (42–72 minutes after sunset, varies by community)
- **Work prohibited:** No use of electricity, no cooking, no travel

**Automation rules:**
- Lights should be automated before candle lighting
- Thermostats should be set beforehand
- Do not schedule any device changes during Shabbat unless pre-programmed

## Passover (Pesach)

- **Duration:** 8 days (7 in Israel)
- **First 2 days and last 2 days:** Yom Tov (full holiday restrictions)
- **Middle 4 days:** Chol HaMoed (intermediate days, some work permitted)
- Yom Tov days carry the same restrictions as Shabbat
- Candle lighting occurs on erev (first night) and the second night

**Automation rule:** Treat the first 2 and last 2 days like Shabbat.

## Rosh Hashanah

**Jewish New Year**

- **Duration:** 2 days (both are Yom Tov)
- Same restrictions as Shabbat
- Shofar (ram's horn) is sounded during daytime
- Candle lighting occurs on both nights
- **Second day candle lighting:** After nightfall of the first day (not before)

**Automation rule:** Treat both days as Shabbat for scheduling.