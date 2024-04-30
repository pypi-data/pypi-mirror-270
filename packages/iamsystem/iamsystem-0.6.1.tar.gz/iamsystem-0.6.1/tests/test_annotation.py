import unittest

from iamsystem.keywords.keywords import Entity
from iamsystem.matcher.annotation import Annotation
from iamsystem.matcher.annotation import _linkedlist_to_list
from iamsystem.matcher.annotation import create_annot
from iamsystem.matcher.annotation import is_ancestor_annot_of
from iamsystem.matcher.annotation import rm_nested_annots
from iamsystem.matcher.annotation import sort_annot
from iamsystem.matcher.matcher import Matcher
from iamsystem.matcher.util import StateTransition
from iamsystem.tokenization.span import is_shorter_span_of
from iamsystem.tree.trie import Trie
from tests.utils_detector import get_gauche_el_in_ivg


class AnnotationTest(unittest.TestCase):
    def test_rm_nested_ents_right_overlapping(self):
        """Since 'prostate cancer' overlaps 'cancer', 'cancer' is a nested
        annotation to remove. 'cancer' is right-most token."""
        matcher = Matcher()
        matcher.add_keywords(keywords=["prostate cancer", "cancer"])
        matcher.remove_nested_annots = False
        annots = matcher.annot_text(text="prostate cancer")
        self.assertEqual(2, len(annots))
        annot_2_keep = annots[0]
        self.assertTrue(annot_2_keep.label == "prostate cancer")
        annot_2_remove = annots[1]
        self.assertTrue(annot_2_remove.label == "cancer")
        annots_filt = rm_nested_annots(annots)
        self.assertTrue(annot_2_remove not in annots_filt)

    def setUp(self) -> None:
        matcher = Matcher()
        ent_prostate_cancer = Entity(label="prostate cancer", kb_id="PK")
        ent_cancer = Entity(label="prostate", kb_id="P")
        matcher.add_keywords(keywords=[ent_cancer, ent_prostate_cancer])
        self.text = "diagnosis of Prostate Cancer"
        matcher.remove_nested_annots = False
        self.annots = matcher.annot_text(text=self.text)
        self.assertEqual(2, len(self.annots))
        self.prostate_annot = self.annots[0]
        self.prostate_cancer_annot = self.annots[1]

    def test_annot_label(self):
        """Check setup assumptions"""
        self.assertEqual(self.prostate_annot.label, "Prostate")
        self.assertEqual(self.prostate_cancer_annot.label, "Prostate Cancer")

    def test_rm_nested_ents_middle(self):
        """Since 'prostate cancer undocumented' overlaps 'cancer',
        'cancer' is a nested annotation to remove.
        Check it work with a middle ent.
        """
        matcher = Matcher()
        matcher.add_keywords(
            keywords=["prostate cancer undocumented", "cancer"]
        )
        matcher.remove_nested_annots = False
        annots = matcher.annot_text(text="prostate cancer undocumented")
        self.assertEqual(2, len(annots))
        annot_2_keep = annots[0]
        self.assertTrue(annot_2_keep.label == "prostate cancer undocumented")
        annot_2_remove = annots[1]
        self.assertTrue(annot_2_remove.label == "cancer")
        annots_filt = rm_nested_annots(annots)
        self.assertTrue(annot_2_remove not in annots_filt)

    def test_rm_nested_ents_left_overlapping(self):
        """Since 'prostate cancer' overlaps 'prostate',
        'prostate' is a nested annotation to remove.
        'prostate' is a left token.
        """
        annot_2_remove = self.prostate_annot
        annot_2_keep = self.prostate_cancer_annot
        annots_filt = rm_nested_annots(self.annots)
        self.assertTrue(annot_2_remove not in annots_filt)
        self.assertTrue(annot_2_keep in annots_filt)

    def test_is_ancestor_annot_of(self):
        """'prostate' node is an ancestor of 'prostate_cancer' in the tree.
        Check 'is_ancestor_annot_of' detects it.
        """
        self.assertTrue(
            is_ancestor_annot_of(
                self.prostate_annot, self.prostate_cancer_annot
            )
        )

    def test_rm_nested_remove_ancestors(self):
        """Check this function remove the ancestor annotation."""
        annots_filt = rm_nested_annots(self.annots, keep_ancestors=False)
        self.assertTrue(self.prostate_annot not in annots_filt)
        self.assertEqual(1, len(annots_filt))

    def test_rm_nested_ents_keep_ancestors(self):
        """Check ancestors are kept when True."""
        annots_filt = rm_nested_annots(self.annots, keep_ancestors=True)
        self.assertEqual(2, len(annots_filt))

    def test_is_shorter_span_of(self):
        """Since 'prostate cancer' overlaps 'prostate',
        'prostate' annotation is a short span."""
        self.assertTrue(
            is_shorter_span_of(self.prostate_annot, self.prostate_cancer_annot)
        )

    def test_sort(self):
        """Test annotation orders by min start values."""
        annots = [self.annots[1], self.annots[0]]
        sort_annot(annots)
        self.assertTrue(annots[0] == self.annots[0])
        self.assertTrue(annots[1] == self.annots[1])

    def test_to_string(self):
        """String representation."""
        annot_string = self.annots[1].to_string()
        self.assertEqual(
            annot_string, "Prostate Cancer\t13 28\tprostate cancer (PK)"
        )

    def test_get_text_substring(self):
        """Offsets are correct and return the correct document's
        substring."""
        text_substring = self.text[
            self.prostate_cancer_annot.start : self.prostate_cancer_annot.end  # noqa
        ]
        self.assertEqual(text_substring, "Prostate Cancer")

    def test_to_string_text(self):
        """Adding text to 'to_string' function add the document's
        substring."""
        annot_string = self.prostate_cancer_annot.to_string(text=self.text)
        self.assertEqual(
            annot_string,
            "Prostate Cancer\t13 28\tprostate cancer (PK)\tProstate Cancer",
        )

    def test_to_string_debug(self):
        """Adding debug=True adds tokens and algorithms names."""
        annot_string = self.prostate_cancer_annot.to_string(debug=True)
        self.assertEqual(
            annot_string,
            "Prostate Cancer\t13 28\tprostate cancer (PK)\tprostate("
            "exact);cancer(exact)",
        )

    def test_create_annot(self):
        """New annotation has the expected attribute values."""
        text = "Insuffisance Ventriculaire  Gauche"
        gauche_node, gauche_el = get_gauche_el_in_ivg()
        ent = Entity("Insuffisance Cardiaque Gauche", "I50.1")
        gauche_node.add_keyword(ent)
        annot: Annotation = create_annot(last_trans=gauche_el, stop_tokens=[])
        self.assertEqual(3, len(annot._tokens))
        self.assertTrue(ent in annot.keywords)
        self.assertEqual(0, annot.start)
        self.assertEqual(34, annot.end)
        self.assertEqual("Insuffisance Ventriculaire Gauche", annot.label)
        substring = text[annot.start : annot.end]  # noqa
        self.assertEqual("Insuffisance Ventriculaire  Gauche", substring)

    def test_is_start_state(self):
        """When parent is none, it's the start_state"""
        trie = Trie()
        start_state = StateTransition.create_first_trans(
            initial_state=trie.get_initial_state()
        )
        self.assertTrue(StateTransition.is_first_trans(start_state))

    def test_transition_state_equality(self):
        """Two transititions states are 'equal' if they have the same
        node number. This equality is important since a 'new' state needs to
        override an existing state."""
        gauche_node, gauche_el = get_gauche_el_in_ivg()
        trans_state_0 = StateTransition(
            previous_trans=None,
            node=gauche_node,
            token=self.annots[0].tokens[0],
            algos=["one"],
            count_not_stopword=0,
        )
        start_state = StateTransition.create_first_trans(
            initial_state=Trie().get_initial_state()
        )
        trans_state_1 = StateTransition(
            previous_trans=start_state,
            node=gauche_node,
            token=None,  # noqa
            algos=["one"],
            count_not_stopword=0,
        )
        self.assertEqual(trans_state_0, trans_state_1)
        trans_set = set()
        trans_set.add(trans_state_0)
        trans_set.discard(trans_state_1)
        trans_set.add(trans_state_1)
        self.assertEqual(len(trans_set), 1)
        for trans in trans_set:
            self.assertTrue(trans.token is None)  # trans_state_1 overrides

    def test_to_dict(self):
        """Check attribute values."""
        gauche_node, gauche_el = get_gauche_el_in_ivg()
        ent = Entity("Insuffisance Cardiaque Gauche", "I50.1")
        gauche_node.add_keyword(ent)
        annot: Annotation = create_annot(last_trans=gauche_el, stop_tokens=[])
        dic = annot.to_dict(text="Another text to check substring is working")
        self.assertEqual(dic["start"], 0)
        self.assertEqual(dic["end"], 34)
        self.assertEqual(dic["label"], "Insuffisance Ventriculaire Gauche")
        self.assertEqual(
            dic["norm_label"], "insuffisance ventriculaire gauche"
        )
        self.assertEqual(len(dic["tokens"]), 3)
        self.assertEqual(len(dic["algos"]), 3)
        self.assertEqual(["Insuffisance Cardiaque Gauche"], dic["kw_labels"])
        self.assertEqual(["I50.1"], dic["kb_ids"])
        self.assertEqual(
            dic["substring"], "Another text to check substring is"
        )
        self.assertEqual(dic["version"], "0.4.0")

    def test_tokens_states_to_list(self):
        """Linked list to list returns the right length."""
        gauche_node, gauche_el = get_gauche_el_in_ivg()
        tokens_states = _linkedlist_to_list(last_el=gauche_el)
        self.assertEqual(3, len(tokens_states))

    def test_node_not_in_final_state(self):
        """Annotation can be created iff a ent is available
        (= node is a final state). Otherwise an exception is raised."""
        gauche_node, gauche_el = get_gauche_el_in_ivg()
        with (self.assertRaises(ValueError)):
            create_annot(last_trans=gauche_el, stop_tokens=[])

    def test_stop_tokens(self):
        """the list of stop_tokens is correct."""
        matcher = Matcher.build(
            keywords=["cancer prostate"], stopwords=["de", "la"]
        )
        annots = matcher.annot_text(text="cancer de la prostate")
        self.assertEqual(2, len(annots[0].stop_tokens))

    def test_stop_tokens_reverse(self):
        """Stopwords z, x, y are inside the annotation but are the last
        tokens when 'order_tokens=True'.It doesn't work if you try to filter
        the stopwords before or in Annotation __init__."""
        matcher = Matcher.build(
            keywords=["cancer prostate"],
            stopwords=["z", "y", "x", "a", "de"],
            order_tokens=True,
            w=3,
        )
        annots = matcher.annot_text(text="a prostate z x y cancer de")
        self.assertEqual(3, len(annots[0].stop_tokens))
        stopwords = [token.label for token in annots[0].stop_tokens]
        self.assertEqual(stopwords, ["z", "x", "y"])
