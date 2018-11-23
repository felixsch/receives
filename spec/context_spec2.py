from expects import expect, be, be_a, be_none, be_true, be_false, equal, contain

from spec.helper import debug, given, settings
from spec.helpers.context import a_context, a_specific_context

from receives.context import to_hash, determine_attribute_type, determine_object_type
from receives.context import Context, ObjectType

from hypothesis.strategies import random_module, text


@given(random_module(), text())
def test_to_hash(m, t):
    expect(to_hash(m, t)).to(equal(to_hash(m, t)))


@given(a_context())
def test_determine_attribute_type(sample):
    attr = getattr(sample.object, sample.attribute)
    expect(determine_attribute_type(sample.object, attr)).to(be(sample.types.attribute))


@given(a_context())
def test_determine_object_type(sample):
    expect(determine_object_type(sample.object)).to(be(sample.types.object))


def test_determine_object_type_invalid():
    x = 1
    expect(determine_object_type(x)).to(be(ObjectType.Variable))
    expect(determine_object_type(debug)).to(be(ObjectType.Method))


@given(a_context())
def test_context_object(sample):
    expect(sample.ctx.object).to(be(sample.object))


@given(a_context())
def test_context_object_type(sample):
    expect(sample.ctx.object_type).to(be(sample.types.object))


@given(a_context())
def test_context_object_name(sample):
    expect(sample.ctx.object_name).to(equal(sample.object_name))


@settings(max_examples=1)
@given(a_specific_context('instance'))
def test_context_base_class(instance):
    expect(instance.ctx.base_class).to(be(instance.object.__class__))


@given(a_context())
def test_context_attribute_name(sample):
    expect(sample.ctx.attribute_name).to(be(sample.attribute))


@given(a_context())
def test_context_attribute_type(sample):
    expect(sample.ctx.attribute_type).to(be(sample.types.attribute))


@given(a_context())
def test_context__hash__(sample):
    expect(hash(sample.ctx)).to(equal(to_hash(sample.object, sample.attribute)))
