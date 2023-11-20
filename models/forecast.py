from dataclasses import dataclass


@dataclass
class Language:
    lang_name: str
    lang_iso: str
    day_text: str
    night_text: str


@dataclass
class Forecast:
    code: int
    day: str
    night: str
    icon: int
    languages: list[Language]

    def get_text_by_lang_code(self, lang_code: str, is_day: int):
        for lang in self.languages:
            if lang.lang_iso == lang_code:
                if is_day == 1:
                    return lang.day_text
                else:
                    return lang.night_text


@dataclass
class ListForecast:
    forecasting: list[Forecast]

    def get_forecast_by_code(self, forecast_code: str) -> Forecast:
        forecast = next((w for w in self.forecasting if w.code == forecast_code), None)
        return forecast
