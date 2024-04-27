
import re

from enum import StrEnum, auto
from dataclasses import dataclass, field


class ThemePeriod(StrEnum):
    EARLY = auto()
    MID = auto()
    LATER = auto()
    ALL = auto()
    ERROR = auto()

    @classmethod
    def has_value(cls, value) -> bool:
        return value in cls._value2member_map_
    
    @classmethod
    def get(cls, value: str, default):
        try:
            return cls[value]
        except KeyError:
            return default


ThemePhaseType = tuple[str, list[str], ThemePeriod]

@dataclass(frozen=True)
class ThemePhase:
    name: str
    subthemes: list[str] = field(default_factory=list)
    period: ThemePeriod = field(default=ThemePeriod.ALL)


class ThemeRules:
    subtheme_pattern = re.compile(r'\(([\w+, ]+)\)')
    phase_combos = ['early', 'mid', 'later', 'early/mid', 'early/later', 'mid/later']

    junk = {r'\)[\/\b\w]': '), ',
            r'\(earlier\)': '(early)',
            r'\(early, later\)': '(early/later)',
            r'\(early\), \b': '(early); ',
            r'\(first album\),': '(early); ',
            r'\(later\), \b': '(later); ',
            r'\);$': ')',
            r'\(deb.\)': '',
            r'themes from ': '',
            r' themes': '',
            r'based on ': '',
            r' \(thematic\)': ''}

    substitutions = {r'\bw\.a\.r\.': 'White Aryan Resistance',
                     r'\bnational socialism\b': 'Nazism',
                     r'\bo9a': 'Order of Nine Angles'}


@dataclass
class Themes:
    full_theme: str
    clean_theme: str = field(init=False)
    phases: list[ThemePhase] = field(init=False)

    def __post_init__(self):
        clean_theme = self.full_theme
        for pattern, substitution in ThemeRules.junk.items():
            clean_theme = re.sub(pattern, substitution, clean_theme, flags=re.IGNORECASE)

        for pattern, substitution in ThemeRules.substitutions.items():
            clean_theme = re.sub(pattern, substitution, clean_theme, flags=re.IGNORECASE)

        del pattern
        del substitution

        phases = clean_theme.split(';')
        phases = list(map(self._parse_phase, map(str.lstrip, phases)))
        phases = self._explode_phases_on_delimiter(phases, '/')
        phases = self._explode_phases_on_delimiter(phases, ',')
        phases = list(map(lambda n: self._parse_subthemes(*n), phases))
        phases = self._remove_duplicates(phases)
        # phases = self._scrub_phases_of_junk(phases)
        self.phases = phases = list(map(lambda n: ThemePhase(*n), phases))
        
        sorted_themes = sorted(phases, key=self._phase_sort_key)
        clean_theme_list = list()
        for phase in sorted_themes:
            theme = phase.name
            if len(phase.subthemes) > 0:
                theme = theme + f' ({", ".join(phase.subthemes)})'
            try:
                _ = clean_theme_list.index(theme)
            except ValueError:
                clean_theme_list.append(theme)

        self.clean_theme = ', '.join(clean_theme_list)

    @staticmethod
    def _phase_sort_key(phase: ThemePhase):
        return (ThemePeriod._member_names_.index(phase.period.name), phase.name)

    @staticmethod
    def _collapse_recurrent_phases(phases: list[ThemePhase]) -> list[ThemePhase]:
        all_phases = set(map(lambda n: n.period, phases))

        phase_counts: dict[str, set[ThemePeriod]] = dict()
        for phase in phases:
            try:
                phase_counts[phase.name].add(phase.period)
            except KeyError:
                phase_counts[phase.name] = {phase.period}

        consistent_themes = set(theme for theme, phases in phase_counts.items() 
                                if phases == all_phases)
        
        collapsed_phases = list(map(lambda n: ThemePhase(n), consistent_themes))
        collapsed_phases += list(filter(lambda p: p.name not in consistent_themes, phases))

        return collapsed_phases

    @staticmethod
    def _scrub_phases_of_junk(phases: list[ThemePhase]) -> list[ThemePhase]:
        raise NotImplementedError
    
    @staticmethod
    def _remove_duplicates(phases: list[ThemePhaseType]) -> list[ThemePhaseType]:
        unique_phases = list()
        for phase in phases:
            
            phase_exists = False
            for existing_phase in unique_phases:
                theme_match = phase[0] == existing_phase[0]
                subthemes_match = phase[1] == existing_phase[1]
                period_match = phase[2] == existing_phase[2]

                phase_exists = theme_match and subthemes_match and period_match
                if phase_exists:
                    break

            if not phase_exists:
                unique_phases.append(phase)

        return unique_phases

    @staticmethod
    def _explode_phases_on_delimiter(phases: list[tuple[str, ThemePeriod]], delimiter: str) -> list[tuple[str, ThemePeriod]]:
        def explode(phase: tuple[str, ThemePeriod]) -> list[tuple[str, ThemePeriod]]:
            name, period = phase
            return [(n.strip(), period) for n in re.split(fr'{delimiter}(?!(?:[^(]*\([^)]*\))*[^()]*\))\s*', name)]

        return sum(list(map(explode, phases)), [])
    
    @staticmethod
    def _parse_subthemes(phase: str, period: ThemePeriod) -> tuple[str, list[str], ThemePeriod]:
        subtheme_pattern = ThemeRules.subtheme_pattern
        subthemes_match = subtheme_pattern.search(phase)
        subthemes = subthemes_match.group(1).split(', ') if subthemes_match else []

        phase = subtheme_pattern.sub('', phase).rstrip()
        return phase, subthemes, period
    
    @staticmethod
    def _parse_phase(phase: str) -> tuple[str, ThemePeriod]:
        phase_patterns = '(' + '|'.join(ThemeRules.phase_combos) + ')'
        phase_match = re.compile(fr'^(?P<name>.*?)(\((?P<period>{phase_patterns})\))?$').match(phase)
        if phase_match is None:
            raise ValueError

        period_text = phase_match.group('period')
        if period_text is not None:
            period = ThemePeriod.get(period_text.upper(), ThemePeriod.ERROR)
        else:
            period = ThemePeriod.ALL

        phase_name = phase_match.group('name')
        return phase_name, period

    def to_dict(self) -> dict:
        phases = [dict(name=p.name.lower(), period=p.period.value) for p in self.phases]
        return dict(theme=self.clean_theme.lower(), theme_phases=phases)
